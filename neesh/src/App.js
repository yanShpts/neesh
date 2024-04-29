import React, { useState, useEffect } from 'react';
import "./main.css";
//import "./Lead.css"

export const Main = () => {
  const [text, setText] = useState([{}])

  useEffect(() => {
    fetch("/pytrends").then(
      res => res.json()
    ).then(
      text => {
        setText(text)
        console.log(text)
      }
    )
  }, [])

  const handleInputChange = (event) => {
    setText(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Logic to submit text to the API (replace with your implementation)

    console.log('Text to submit:', text);
    setText(''); // Clear text input after submission
  };

  return (
    <div className="box">
      <div className="group">
        <div className="text-wrapper">neesh</div>
        <p className="div">How niche is your interest?</p>
        <form onSubmit={handleSubmit}> {}
          <textarea 
            className="rectangle" 
            value={text} 
            onChange={handleInputChange} 
          />
          <button type="submit" className="submit-button">Submit</button>
        </form>
      </div>
    </div>
  );
};

export const Lists = () => {
  return(
    <div className='scores'>
      <div className='Leaderboard'>
        <div className='title'>Leaderboard</div>
        <ul className='list'>
          <li>Item: Score</li>
          <li>Item: Score</li>
          <li>Item: Score</li>
          <li>Item: Score</li>
          <li>Item: Score</li>
        </ul>
      </div>
      <div className='Leaderboard'>
        <div className='title'>Last Entries</div>
        <ul className='list'>
          <li>Item: Score</li>
          <li>Item: Score</li>
          <li>Item: Score</li>
          <li>Item: Score</li>
          <li>Item: Score</li>
        </ul>
      </div>
    </div>


  )
}