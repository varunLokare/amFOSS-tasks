import React from 'react';

export default function MovieModal({ movie, onClose }) {
  if (!movie) return null;

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="close-btn" onClick={onClose}>&times;</button>
        <h2 style={{ color: '#f59e0b', marginBottom: '0.5rem' }}>{movie.title}</h2>
        <p style={{ color: '#9ca3af', marginBottom: '1rem' }}>
          Release: {movie.release_date || 'Unknown'} | Rating: ⭐ {movie.vote_average ? movie.vote_average.toFixed(1) : 'N/A'}/10
        </p>
        <h4 style={{ marginBottom: '0.5rem' }}>Historical Summary:</h4>
        <p style={{ lineHeight: '1.6', color: '#d1d5db' }}>
          {movie.overview || 'No archival record found for this entry.'}
        </p>
      </div>
    </div>
  );
}