import React from 'react';
import AppBar from './components/AppBar';
import EmployeeList from './components/EmployeeList';
import FileUploader from './components/FileUploader';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { result: "" };
    this.handleChangeResult = this.handleChangeResult.bind(this);
  }

  handleChangeResult(result) {
    this.setState({ result: result })
  }

  render() {
    return (
      <div className="App">
        <AppBar />
        <br/>
        <div className='upload'>
          <h2> ファイル送信 </h2>
          <FileUploader onChangeResult={this.handleChangeResult} />
        </div>
        <div className='result'>
          <h2> 結果 </h2>
          {
              this.state.result !== "" &&
              <EmployeeList result={this.state.result} />
          }
        </div>
      </div>
    );
  }
}

export default App;