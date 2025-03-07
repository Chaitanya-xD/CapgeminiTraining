import './App.css';
import Header from './components/header.js';
import Body from './components/body.js';
import Footer from './components/footer.js';
import InterestCalculator from './components/calculator.js';

function App() {
  return (
    <div className="App">
      <Header/>
      <Body/>
      <InterestCalculator/>
      <Footer/>
    </div>
  );
}

export default App;
