import React, { useReducer, useState } from "react";
import "./App.css";

const formReducer = (state, event) => {
    return {
        ...state,
        [event.name]: event.value,
    };
};

function App() {
    const [formData, setFormData] = useReducer(formReducer, {});
    const [submitting, setSubmitting] = useState(false);

    const handleSubmit = async (event) => {
        event.preventDefault();
        setSubmitting(true);
        console.log(formData);
        const newBook = await fetch("http://127.0.0.1:8000/books/create/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        });
        console.log(newBook);
        setTimeout(() => {
            setSubmitting(false);
        }, 3000);
    };

    const handleChange = (event) => {
        setFormData({
            name: event.target.name,
            value: event.target.value,
        });
    };

    return (
        <div className="wrapper">
            <h1>Book Fields</h1>
            {submitting && (
                <div>
                    Submtting Book information... You are submitting the
                    following:
                    <ul>
                        {Object.entries(formData).map(([name, value]) => (
                            <li key={name}>
                                <strong>{name} </strong> : {value.toString()}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
            <form onSubmit={handleSubmit}>
                <fieldset>
                    <label>
                        <p>Book Title:</p>
                        <input name="name" onChange={handleChange} />
                    </label>
                    <label>
                        <p>Author:</p>
                        <input name="author" onChange={handleChange} />
                    </label>
                    <label>
                        <p>Publisher:</p>
                        <input name="publisher" onChange={handleChange} />
                    </label>
                    <label>
                        <p>ISBN:</p>
                        <input name="ISBN" onChange={handleChange} />
                    </label>
                    <label>
                        <p>Date Published:</p>
                        <input
                            type="datetime-local"
                            name="date_pub"
                            onChange={handleChange}
                        />
                    </label>
                </fieldset>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

export default App;
