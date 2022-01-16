import AppBar from './components/AppBar';
import EmployeeList from './components/EmployeeList';
import './App.css';

function App() {
  return (
    <div className="App">
      <AppBar />
      <br/>
      <p class="fs-2"> 従業員一覧 </p>
      <EmployeeList />
    </div>
  );
}

export default App;