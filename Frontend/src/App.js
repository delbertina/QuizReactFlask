import './App.scss';
import React, { Component } from 'react';
import Card from './components/card/card.js';
import Alerts from './components/alerts/alerts.js';
import Header from './components/header/header.js';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = { alertDisplay: '', totalCorrect: 0 };
    this.childCard = React.createRef();
  }

  handleAlertChange(alert, totalCorrect) {
    this.setState({ alertDisplay: alert, totalCorrect: totalCorrect });
    if (alert === 'correct' || alert === 'incorrect') {
      setTimeout(() => {
        this.setState({ alertDisplay: '' });
      }, 1500);
    }
  }

  handleStartOver() {
    this.childCard.current.restartQuiz();
  }

  render() {
    return (
      <div>
        <Header />
        <div className="main">
          <div className="alert-wrapper">
            <Alerts alertDisplay={this.state.alertDisplay} totalCorrect={this.state.totalCorrect} />
          </div>
          <div className="card-wrapper">
            <Card onAlertChange={this.handleAlertChange.bind(this)} ref={this.childCard} />
          </div>
          <div className="page-actions">
            <button className="start-over-button" onClick={() => { this.handleStartOver() }}>
              Start Over
            </button>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
