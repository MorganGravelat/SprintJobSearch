import React, { useState } from 'react'
import QuestionForm from './components/QuestionForm'
import logo from './logo.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const handleSubmit = (name: string, question: string) => {
    console.log(`Name: ${name}, Question: ${question}`);
  };

  return (
    <div className="App">
      <QuestionForm />
    </div>
  )
}

export default App
