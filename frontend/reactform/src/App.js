import React, { useReducer, useState } from 'react';
import './App.css';

const formReducer = (state, event) => {
 return {
   ...state,
   [event.name]: event.value
 }
}

function App() {
  const [formData, setFormData] = useReducer(formReducer, {});
  const [submitting, setSubmitting] = useState(false);

  const handleSubmit = event => {
    event.preventDefault();
    setSubmitting(true);

    setTimeout(() => {
      setSubmitting(false);
    }, 3000)
  }

  const handleChange = event => {
    setFormData({
      name: event.target.name,
      value: event.target.value,
    });
  }

  return(
    <div className="wrapper">
      <h1>Book Submission Form</h1>
      {submitting &&
        <div>Submtting Book information...
          You are submitting the following:
         <ul>
           {Object.entries(formData).map(([name, value]) => (
             <li key={name}><strong>{name} </strong> : {value.toString()}</li>
           ))}
         </ul>
        </div>
      }
      <form onSubmit={handleSubmit}>
        <fieldset>

          <label>
            <p>Book Title</p>
            <input name="name" onChange={handleChange}/>
          </label>

          <label>
            <p>Author(s)</p>
            <input name="authors" onChange={handleChange}/>
          </label>

          <label>
            <p>ISBN</p>
            <input name="isbn" onChange={handleChange}/>
          </label>

          <label>
            <p>Publisher(s)</p>
            <input name="publishers" onChange={handleChange}/>
          </label>

          <label>
            <p>Date Published</p>
            <input type="date" name="yearpublished" onChange={handleChange}/>
          </label>
       </fieldset>

        <button type="submit">Submit</button>
      </form>

    </div>
  )
}

export default App;