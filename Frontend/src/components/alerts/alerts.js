import React, { Component } from 'react';
import './alerts.scss';


function CorrectAlert() {
    return <div className="correct-alert alert">
        <h3>Correct!</h3>
    </div>;
}
function IncorrectAlert() {
    return <div className="incorrect-alert alert">
        <h3>Incorrect!</h3>
    </div>;
}
class DoneAlert extends Component {
    render() {
        return <div className="done-alert alert">
            <h3>Results: {((this.props.totalCorrect / 15) * 100).toFixed(1)}% {this.props.totalCorrect}/15</h3>
        </div>;
    }
}
class DisplayAlert extends Component {
    render() {
        if (this.props.alertDisplay === 'correct') {
            return <CorrectAlert />;
        } else if (this.props.alertDisplay === 'incorrect') {
            return <IncorrectAlert />;
        } else if (this.props.alertDisplay === 'done') {
            return <DoneAlert totalCorrect={this.props.totalCorrect} />;
        } else {
            return null;
        }
    }
}

class Alerts extends Component {

    render() {
        return (
            <div className="alert-list">
                <DisplayAlert alertDisplay={this.props.alertDisplay} totalCorrect={this.props.totalCorrect} />
            </div>
        );
    }
}

export default Alerts;