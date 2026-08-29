import React, { useState, useEffect } from 'react';
import MovieCard from './components/MovieCard';
import MovieModal from './components/MovieModal';

const API_KEY = import.meta.env.VITE_TMDB_API_KEY;
const API_BASE = 'https://api.themoviedb.org/3';

export default function App() {
  const [movies, setMovies] = useState([]);
  const [query, setQuery] = useState('');
  const [activeTab, setActiveTab] = useState('discover');
  const [selectedMovie, setSelectedMovie] = useState(null);

  const [watchlist, setWatchlist] = useState(() => {
    try {
      const saved = localStorage.getItem('ohara_watchlist');
      return saved ? JSON.parse(saved) : [];
    } catch (e) {
      return [];
    }
  });

  useEffect(() => {
    localStorage.setItem('ohara_watchlist', JSON.stringify(watchlist));
  }, [watchlist]);

  useEffect(() => {
    fetchTrendingMovies();
  }, []);

  const fetchTrendingMovies = async () => {
    try {
      const res = await fetch(`${API_BASE}/movie/popular?api_key=${API_KEY}`);
      const data = await res.json();
      setMovies(data.results || []);
    } catch (err) {
      console.error('Failed to fetch movies:', err);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    try {
      const res = await fetch(`${API_BASE}/search/movie?api_key=${API_KEY}&query=${encodeURIComponent(query)}`);
      const data = await res.json();
      setMovies(data.results || []);
      setActiveTab('discover');
    } catch (err) {
      console.error('Failed to search:', err);
    }
  };

  const toggleWatchlist = (movie) => {
    const exists = watchlist.some((m) => m.id === movie.id);
    if (exists) {
      setWatchlist(watchlist.filter((m) => m.id !== movie.id));
    } else {
      setWatchlist([...watchlist, movie]);
    }
  };

  const displayedMovies = activeTab === 'discover' ? movies : watchlist;

  return (
    <div className="container">
      <header>
        <div className="logo-area">
          <h1>THE OHARA ARCHIVE</h1>
          <p>Preserving Cinematic History Across the Grand Line</p>
        </div>
        <div className="nav-buttons">
          <button
            className={activeTab === 'discover' ? 'active' : ''}
            onClick={() => setActiveTab('discover')}
          >
            Discover
          </button>
          <button
            className={activeTab === 'watchlist' ? 'active' : ''}
            onClick={() => setActiveTab('watchlist')}
          >
            My Watchlist ({watchlist.length})
          </button>
        </div>
      </header>

      {activeTab === 'discover' && (
        <form className="search-bar" onSubmit={handleSearch}>
          <input
            type="text"
            placeholder="Search records by title..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button type="submit">Search</button>
        </form>
      )}

      {displayedMovies.length === 0 ? (
        <div style={{ textAlign: 'center', color: '#9ca3af', marginTop: '3rem' }}>
          {activeTab === 'watchlist' ? 'Your archive is empty. Add movies to preserve them!' : 'No records found.'}
        </div>
      ) : (
        <div className="movie-grid">
          {displayedMovies.map((movie) => (
            <MovieCard
              key={movie.id}
              movie={movie}
              isSaved={watchlist.some((m) => m.id === movie.id)}
              onToggleWatchlist={toggleWatchlist}
              onSelect={(m) => setSelectedMovie(m)}
            />
          ))}
        </div>
      )}

      {selectedMovie && (
        <MovieModal
          movie={selectedMovie}
          onClose={() => setSelectedMovie(null)}
        />
      )}
    </div>
  );
}