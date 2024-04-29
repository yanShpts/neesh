import React, { useState, useEffect } from 'react';
import axios from 'axios';
import "./main.css";

const App = () => {
  const [inputText, setInputText] = useState('');
  const [score, setScore] = useState(null);
  const [last5Entries, setLast5Entries] = useState();

  const calculateScore = async () => {
    try {
      const response = await axios.post('http://localhost:5000/pytrends', {text: inputText});
      console.log(response);
      const interest = response.data; //TO BE IMPLEMENTED (get score somehow)
      const score = interest[0].score;
      setScore(score);
    }
    catch (error) {
      console.error('Error calculating niche score:', error);
    }
  }


  async function submit(e){
    if(e.key === 'Enter'){
      e.preventDefault();
      calculateScore(inputText);
    }
  }

  useEffect(() => {
    async function getLast5Entries() {
      try{ 
        const response = await fetch('http://localhost:5000/get_last_5');
        const data = await response.json();
        setLast5Entries(data);
      }
      catch (error) {
        console.error('Error fetching last 5 entries:', error);
      }
    }

    getLast5Entries();
  },[])

  return (
    <div style={{ textAlign: 'center', marginTop: '20vh'}}>
      <h1>Neesh</h1>
      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        onKeyDown= {(e) => submit(e)}
        placeholder="How niche is your interest?"
        style={{resize: 'none', width: '60%', padding: '8px', marginBottom: '10px'}}
      />
      <hr style={{border: "none"}}></hr>
      <button onKeyDown={e => e.key === 'Enter' ? calculateScore: ''} 
        onClick={calculateScore} 
        style={{width: "200px", height: "50px", border: "none", borderRadius: "100px", padding: '8px', cursor: 'pointer' }}>
        <b>Calculate Niche Score</b>
      </button>
      {score !== null && (
        <div style={{ marginTop: '10px' }}>
          <p>Score: {score}</p>
        </div>
      )}
      {last5Entries && (
        <div style={{textAlign: 'center', marginTop: '20px' }}>
          <h2>Last 5 Entries</h2>
          <ul style={{display: 'inline-block', textAlign: 'left' }}>
            {last5Entries.map((entry, index) => (
              <li key={index}>
                <p>Score: {entry.score}, Interest: {entry.interest}</p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default App;