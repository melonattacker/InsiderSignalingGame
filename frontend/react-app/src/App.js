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
        <p class="fs-3"> CSVファイル送信 </p>
        <FileUploader onChangeResult={this.handleChangeResult} />
        <br/>
        <p class="fs-3"> 結果 </p>
        <EmployeeList result={this.state.result} />
      </div>
    );
  }
}

export default App;