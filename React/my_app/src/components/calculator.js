import React, {useState} from 'react'; 


function InterestCalculator() {
  const[principal, setPrincipal] = useState("")
  const[rate, setRate] = useState("")
  const[time, setTime] = useState("")
  const[type, setType] = useState("")
  const[result, setResult] = useState("")

  const calculateInterest = () => { 
    let P = parseFloat(principal);
    let r = parseFloat(rate);
    let t = parseFloat(time);
  
    if( isNaN(P) || isNaN(r) || isNaN(t) || P <= 0 || r <= 0 || t <= 0 ) {
      setResult("Please enter valid value!")
    }

    let interest = 0;
    if( type === 'simple' ){
      interest = (P*t*r)/100;
    }
    else {
      interest = P*(Math.pow())
    }
  }

  return (
    <div style={styles.container}>
      <h2>Interest Calculator</h2>
      <label>Principal (P):</label>
      <input 
      type="number"
      value={principal}
      onChange={(e)=>setPrincipal(e.target.value)}
      style={styles.input}
      placeholder="Enter Principal amount"
      />

      <label>Rate of Interest(R):</label>
      <input 
      type="number"
      value={rate}
      onChange={(e)=>setRate(e.target.value)}
      style={styles.input}
      placeholder="Enter Rate of Interest"
      />

      <label>Time (T):</label>
      <input 
      type="number"
      value={time}
      onChange={(e)=>setTime(e.target.value)}
      style={styles.input}
      placeholder="Enter Time(Years)"
      />

      <select>
        <option disabled selected>Select</option>
        <option value="simple">Simple</option>
        <option value="compound">Compound</option>
      </select>
    </div>
  );
}


const styles = {
  
}


export default InterestCalculator;