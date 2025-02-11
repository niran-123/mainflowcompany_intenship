import React, { useState, useEffect } from "react";
import axios from "axios";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import MovieDetail from "./MovieDetail";
import "tailwindcss/tailwind.css";

const API_KEY = "YOUR_API_KEY";
const BASE_URL = "https://api.themoviedb.org/3";

const App = () => {
  return (
    <Router>
      <div className="bg-gray-900 min-h-screen text-white p-4">
        <h1 className="text-3xl text-center font-bold mb-6">Movie Explorer</h1>
        <Routes>
          <Route path="/" element={<MovieList />} />
          <Route path="/movie/:id" element={<MovieDetail />} />
        </Routes>
      </div>
    </Router>
  );
};

const MovieList = () => {
  const [movies, setMovies] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    axios.get(`${BASE_URL}/movie/popular?api_key=${API_KEY}`)
      .then(res => setMovies(res.data.results))
      .catch(err => console.error(err));
  }, []);

  const handleSearch = (e) => {
    e.preventDefault();
    axios.get(`${BASE_URL}/search/movie?api_key=${API_KEY}&query=${search}`)
      .then(res => setMovies(res.data.results))
      .catch(err => console.error(err));
  };

  return (
    <div className="container mx-auto">
      <form onSubmit={handleSearch} className="mb-6 text-center">
        <input
          type="text"
          placeholder="Search Movies..."
          className="p-2 text-black rounded-l-lg"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <button type="submit" className="bg-blue-500 px-4 py-2 rounded-r-lg">Search</button>
      </form>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {movies.map(movie => (
          <Link key={movie.id} to={`/movie/${movie.id}`} className="block">
            <div className="bg-gray-800 p-4 rounded-lg">
              <img src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`} alt={movie.title} className="w-full rounded-md" />
              <h2 className="text-lg font-bold mt-2">{movie.title}</h2>
              <p>⭐ {movie.vote_average}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default App;
