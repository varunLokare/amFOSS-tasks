import React from 'react';

const IMG_BASE_URL = 'https://image.tmdb.org/t/p/w500';

export default function MovieCard({ movie, isSaved, onToggleWatchlist, onSelect }) {
  const posterPath = movie.poster_path
    ? `${IMG_BASE_URL}${movie.poster_path}`
    : 'https://via.placeholder.com/500x750?text=No+Poster+Found';

  return (
    <div className="movie-card">
      <div className="poster-wrapper" onClick={() => onSelect(movie)} style={{ cursor: 'pointer' }}>
        <img src={posterPath} alt={movie.title} />
      </div>

      <div className="movie-info">
        <div>
          <h3 className="movie-title">{movie.title}</h3>
          <div className="movie-meta">
            <span>{movie.release_date ? movie.release_date.split('-')[0] : 'N/A'}</span>
            <span>⭐ {movie.vote_average ? movie.vote_average.toFixed(1) : 'N/A'}</span>
          </div>
        </div>

        <button
          className={`btn-watchlist ${isSaved ? 'in-watchlist' : ''}`}
          onClick={() => onToggleWatchlist(movie)}
        >
          {isSaved ? 'Remove from Archive' : '+ Add to Archive'}
        </button>
      </div>
    </div>
  );
}