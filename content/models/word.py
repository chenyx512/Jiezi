from django.db import models
from django.core.exceptions import ValidationError
import unicodedata

from content.models import GeneralContentModel, OrderableMixin


class DefinitionInWord(OrderableMixin):
    class PartOfSpeech(models.TextChoices):
        __empty__ = 'TODO'
        ADJ = 'adj', 'adjective'
        ADV = 'adv', 'adverb'
        CONJ = 'conj', 'conjunction'
        INTERJ = 'interj', 'interjection'
        M = 'm', 'measure word'
        MV = 'mv', 'modal verb'
        N = 'n', 'noun'
        NU = 'nu', 'numeral'
        P = 'p', 'particle'
        PN = 'pn', 'proper noun'
        PR = 'pr', 'pronoun'
        PREFIX = 'prefix', 'prefix'
        PREP = 'prep', 'preposition'
        QP = 'qp', 'question particle'
        QPR = 'qpr', 'question pronoun'
        T = 't', 'time word'
        V = 'v', 'verb'
        VC = 'vc', 'verb plus complement'
        VO = 'vo', 'verb plus object'

    word = models.ForeignKey('Word', on_delete=models.CASCADE,
                             related_name='definitions',
                             related_query_name='definition')
    part_of_speech = models.CharField(max_length=6,
                                      choices=PartOfSpeech.choices,
                                      blank=True)
    definition = models.CharField(max_length=70,
                                  blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.part_of_speech} {self.definition}"

    def __repr__(self):
        return f"<Def of {self.word}: {str(self)}>"


class CharacterInWord(OrderableMixin):
    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    word = models.ForeignKey('Word', on_delete=models.CASCADE)

    class Meta:
        ordering = ['order']
        unique_together = ['character', 'word', 'order']


class Sentence(OrderableMixin):
    word = models.ForeignKey('Word', on_delete=models.CASCADE,
                             related_name='sentences',
                             related_query_name='sentence')
    pinyin = models.CharField(max_length=200)
    chinese = models.CharField(max_length=40)
    translation = models.CharField(max_length=200)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.chinese

    def __repr__(self):
        return f"<EgSent of {self.word}: {str(self)}>"


class Word(GeneralContentModel):
    chinese = models.CharField(max_length=5)
    identifier = models.CharField(max_length=10, blank=True)

    pinyin = models.CharField(max_length=36, default='TODO')

    characters = models.ManyToManyField('Character',
                                        related_name='words',
                                        related_query_name='word',
                                        through='CharacterInWord')
    memory_aid = models.TextField(max_length=300,
                                  blank=True, default='TODO')

    class Meta:
        unique_together = ['chinese', 'identifier']

    def clean(self):
        """check that word and characters do not mismatch in chinese & pinyin"""

        def unaccent(x):
            return unicodedata.normalize('NFKD', x).encode('ascii','ignore')

        super().clean()
        if self.is_done:
            if not self.characters.exists():
                raise ValidationError('cannot be done without any character')

            len_chinese = len(self.chinese)
            len_character = self.characters.count()
            if len_character != len_chinese:
                raise ValidationError(f"length mismatch between chinese "
                    f"{len_chinese} and characters {len_character}")

            word_pinyin = self.pinyin.replace(' ', '')
            character_pinyin = ''
            for index, (chinese, character) in \
                    enumerate(zip(self.chinese, self.characters.all())):
                if chinese != character.chinese:
                    raise ValidationError(f"mismatch at index {index}: chinese "
                        f"is {chinese} but character is {character}")
                character_pinyin += character.pinyin
            word_pinyin = unaccent(word_pinyin)
            character_pinyin = unaccent(character_pinyin)
            raise ValidationError(f"mismatch of pinyin, word gives {word_pinyin}"
                                  f" but character gives {character_pinyin}")

    def get_child_models(self):
        characters = list(self.characters.all())
        return [('characters', c) for c in characters]

    def save(self, *args, **kwargs):
        adding = self._state.adding
        super().save(*args, **kwargs)
        if adding: # if adding, connect the necessary characters
            from content.models import Character
            for index, chinese in enumerate(self.chinese):
                characters = Character.objects.filter(chinese=chinese)
                cnt = characters.count()
                if cnt == 1:
                    character = characters.get()
                elif cnt > 1:
                    character = Character.get_TODO_character()
                else:
                    character = Character.objects.get_or_create(
                        chinese=chinese)[0]
                CharacterInWord.objects.create(character=character,
                                               word=self, order=index)

        OrderableMixin.reset_order(self.characterinword_set)
        OrderableMixin.reset_order(self.sentences)
        OrderableMixin.reset_order(self.definitions)

    def __str__(self):
        if self.identifier:
            return f"{self.chinese}({self.identifier})"
        else:
            return self.chinese

    def __repr__(self):
        return f"<W{self.id:04d}:{self.chinese}#{self.identifier}>"