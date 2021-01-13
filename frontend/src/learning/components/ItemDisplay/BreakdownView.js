import React from 'react';
import 'core-js/stable';
import 'regenerator-runtime/runtime';
import PropTypes from 'prop-types';
import styled from 'styled-components';

import RelatedItems from './RelatedItems.js';
import { RadImage } from './RadicalDisplay/RadDisplay.js';
import ItemPhonetic from './ItemPhonetic.js';

import useLoadRad from '@learning.hooks/useLoadRad.js';
import useLoadChar from '@learning.hooks/useLoadChar.js';

import PopUp from './WordDisplay/PopUp';

const Row = styled.div`
    display: inline-flex;
    min-width: 100%;
    justify-content: space-evenly;
    align-items: center;
    flex-wrap: nowrap;
    margin-bottom: 20px;

    @media only screen and (max-width: 480px) {
        flex-wrap: wrap;
    }
`;

const MnemonicImageWrapper = styled.div`
    width: 35%;
    min-width: 60px;
    max-height: 150px;
    object-fit: contain;
    font-size: 2.25em;
    text-align: center;
`;

const RadDefinition = styled.h4`
    display: inline-block;
    width: 60%;
    font-size: 1.2em;
    text-align: center;
    min-width: 60px;
    margin-top: 15px;
`;
//
/** Render a single character breakdown display using the
 * radical in props.url. Re-render automatically when props.url
 * updates to a new value.
 */
function BreakdownRad(props) {

    const radical = useLoadRad(props.url);

    const renderRadical = (radical) => {
        const chinese = radical.chinese;
        const def = radical.explanation;
        const imageUrl = radical.image;

        return (
            <>
                <Row>
                    <MnemonicImageWrapper>
                        <RadImage url={imageUrl}
                            radical={chinese}/>
                    </MnemonicImageWrapper> 
                    <RadDefinition className='use-serifs'>
                        {def}
                    </RadDefinition>
                </Row>
                <RelatedItems 
                    items={radical.related_characters}
                    item={radical.chinese}
                    itemType='character' />
            </>
        );
    };

    if (radical === null) {
        return 'Loading character data';
    } else {
        return renderRadical(radical);
    }
}

BreakdownRad.propTypes = {
    url: PropTypes.string.isRequired
};

const CharDefList = styled.ul`

    padding-left: 10px;
    font-size: 1.3em;

    @media only screen and (max-width: 480px) {
        padding: 0;
    }
`;

const CharDefListItem = styled.li`
    line-height: 1.75em;
`;

/** 
 * Render a single word breakdown display using the
 * character in props.url. Re-render automatically 
 * when props.url updates to a new value.
 */
function BreakdownChar(props) {

    const character = useLoadChar(props.url);

    const renderDefinitions = (definitions) => {
        return (
            <CharDefList>
                { definitions.map( (elem, i) => {
                    return (
                        <CharDefListItem 
                            key={i}
                            className='use-serifs'
                        >
                            {elem}
                        </CharDefListItem>
                    );
                })}
            </CharDefList>
        );
    };

    const renderCharacter = (character) => {
        const definitions = character.definitions.map( v => 
            v.definition
        );
        return (
            <>

                {/* This should be optimized (character is
                    loaded twice) */}
                <PopUp
                    contentURL = {props.url}
                />

                <Row>
                    <ItemPhonetic pinyin={character.pinyin}
                        audioURL={character.audio}
                        item={character.chinese}
                    />
                    {renderDefinitions(definitions)}
                </Row>
                {/* Added items (related_words) as a props */}
                <RelatedItems 
                    items={character.related_words}
                    item={character.chinese}
                    itemType='word' 
                />
            </>
        );
    };

    if (character === null) {
        return 'Loading character data';
    } else {
        return renderCharacter(character);
    }
}

BreakdownChar.propTypes = {
    url: PropTypes.string.isRequired
};

const MemoryAidHeading = styled.h2`
    display: inline-block;
    width: 100%;
    color: var(--teritary-text);
    font-size: 0.9em;
    font-weight: 400;
    text-align: center;
    margin: 20px auto 10px;
`;

const MemoryAidContent = styled.div`
    width: 100%;
    font-size: 0.9em;
    color: var(--secondary-text);
    border-radius: 5px;
    padding: 15px 20px;
    font-weight: 400;
`;

/**
 * Renders a <MemoryAidView /> component.
 */
function MemoryAidView(props) {

    const content =  props.content;

    if (content != null && content != '' 
            && content != 'TODO' ) {
        return (
            <>
                <MemoryAidHeading>
                    Memory Aid
                </MemoryAidHeading>
                <MemoryAidContent className='box-shadow'>
                    {props.content}
                </MemoryAidContent>
            </>
        );
    } else { return null; }
}

MemoryAidView.propTypes = {
    /** The associated memory aid sentence. */
    content: PropTypes.string
};

/** Renders a breakdown view for a word or character */
export default class BreakdownView extends React.Component {

    static propTypes = {
        /** The type of breakdown components. */
        type: PropTypes.oneOf(['radical', 'word']),

        /** URLs of the breakdown components. */
        componentURL: PropTypes.arrayOf(PropTypes.string),

        /** The associated memory aid sentence. */
        memoryAid: PropTypes.string
    }

    constructor(props) {
        super(props);
        this.state = {
            show: false
        };
    }

    /**
     * Render the character breakdown for each radical 
     * specified in the urls.
     * @param {[String]} urls 
     */
    renderBreakdownRad(urls) {
        // It is possible to have two breakdown items with the
        // same content (and url), and therefore we cannot use
        // url as the key.
        return urls.map( (url, i) => 
            (
                <div key={i}
                    className='breakdown-card box-shadow'>
                    <BreakdownRad url={url} />
                </div>
            )
        );
    }
    //
    /**
     * Render the word breakdown for each character 
     * specified in the urls.
     * @param {[String]} urls 
     */
    renderBreakdownChar(urls) {
        // It is possible to have two breakdown items with the
        // same content (and url), and therefore we cannot use
        // url as the key.
        return urls.map( (url, i) => 
            (
                <div key={i}
                    className='breakdown-card box-shadow'>
                    <BreakdownChar url={url} />
                </div>
            )
        );
    }

    toggle = () => {
        this.setState( prev => ({show: !prev.show}));
    }

    render() {
        const type = this.props.type;
        const toggleTitle = type + ' breakdown';
        const urls = this.props.componentURL;

        return (
            <div className='breakdown-container'>
                <div 
                    className={'breakdown-toggle ' + (
                        this.state.show ? 'toggled' : ''
                    )}
                    onClick={this.toggle}>
                    <h4>
                        {(this.state.show ? 'Close ' : 'Show me the ') +
                            toggleTitle
                        }
                    </h4>
                    <i className={
                        'fas fa-chevron-down ' + 
                        (this.state.show ? 'inversed' : '')} >
                    </i>
                </div>
                <div 
                    className={'breakdown-content ' + (
                        this.state.show ? 'show' : ''
                    )}>

                    { type == 'radical' ?
                        this.renderBreakdownRad(urls) :
                        this.renderBreakdownChar(urls)
                    } 

                    <MemoryAidView
                        content={this.props.memoryAid}/>
                </div>
            </div>
        );
    }
}
