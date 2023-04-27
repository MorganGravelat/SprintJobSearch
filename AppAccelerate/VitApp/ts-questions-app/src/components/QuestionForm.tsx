import React, { useEffect, useState } from "react";
import "./css/QuestionForm.css";

const QuestionForm: React.FC = () => {
  const [name, setName] = useState("");
  const [question, setQuestion] = useState("");
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log(name);
    console.log(question);
    setName("");
    setQuestion("");
  };


  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <label>
        Question:
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
};
export default QuestionForm;
