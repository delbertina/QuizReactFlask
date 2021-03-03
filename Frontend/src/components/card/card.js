import React, { Component } from 'react';
import './card.scss';

class Card extends Component {

    constructor(props) {
        super(props);
        this.state = {
            totalCorrect: 0,
            correctId: 0,
            questionNum: 0,
            questionText: '',
            possibleAnswers: ['', '', '', ''],
            isLoading: false
        };
    }

    componentDidMount() {
        this.nextQuestion();
    }

    handleClick(index) {
        if (index === this.state.correctId) {
            this.props.onAlertChange('correct');
            this.setState({
                totalCorrect: this.state.totalCorrect + 1,
            });
        } else {
            this.props.onAlertChange('incorrect');
        }
        setTimeout(() => {
            this.nextQuestion();
        }, 2000);
    }

    nextQuestion() {
        this.setState({ isLoading: true });
        fetch('http://127.0.0.1:5000/api/random_question/')
            .then(res => res.json())
            .then((data) => {
                this.setState({
                    correctId: data.correctId,
                    questionNum: this.state.questionNum + 1,
                    questionText: data.question,
                    possibleAnswers: data.answers,
                    isLoading: false
                });
                if (this.state.questionNum > 15) {
                    this.restartQuiz();
                }
            }).catch(console.log);
    }

    restartQuiz() {
        this.props.onAlertChange('done', this.state.totalCorrect);
        setTimeout(() => {
            this.props.onAlertChange('');
        }, 1500);
        this.setState({
            totalCorrect: 0,
            questionNum: 0,
        });
        this.nextQuestion();
    }

    render() {
        return (
            <div className="card" >
                <div className="card-header">
                    <h3>
                        Question #{this.state.questionNum}
                    </h3>
                    <p>
                        {this.state.totalCorrect} / 15
                    </p>
                </div>
                <div className="card-content">
                    <p>
                        {this.state.questionText}
                    </p>
                </div>
                <div className="card-actions">
                    <button
                        onClick={() => { this.handleClick(0) }}
                        disabled={this.state.isLoading}
                        className={`answer-button 
                        ${this.state.correctId === 0
                                ? "correct-button"
                                : "incorrect-button"}`}
                    >
                        A) {this.state.possibleAnswers[0]}
                    </button>
                    <button
                        onClick={() => { this.handleClick(1) }}
                        disabled={this.state.isLoading}
                        className={`answer-button 
                        ${this.state.correctId === 1
                                ? "correct-button"
                                : "incorrect-button"}`}
                    >
                        B) {this.state.possibleAnswers[1]}
                    </button>
                    <button
                        onClick={() => { this.handleClick(2) }}
                        disabled={this.state.isLoading}
                        className={`answer-button 
                        ${this.state.correctId === 2
                                ? "correct-button"
                                : "incorrect-button"}`}
                    >
                        C) {this.state.possibleAnswers[2]}
                    </button>
                    <button
                        onClick={() => { this.handleClick(3) }}
                        disabled={this.state.isLoading}
                        className={`answer-button 
                        ${this.state.correctId === 3
                                ? "correct-button"
                                : "incorrect-button"}`}
                    >
                        D) {this.state.possibleAnswers[3]}
                    </button>
                </div>
            </div>
        );
    }
}

export default Card;