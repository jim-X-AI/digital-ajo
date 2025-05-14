import React from 'react';
import { useParams } from 'react-router-dom';
import '../styles/HistoryPage.css';

function HistoryPage() {
  const { id } = useParams();
  console.log("Group ID:", id); // Now using the id parameter

  // Mock data - in a real app, this would come from an API
  const history = [
    { date: "2023-05-01", recipient: "Aisha", proofs: ["proof1.jpg", "proof2.jpg"] },
    { date: "2023-04-15", recipient: "Chukwuemeka", proofs: ["proof3.jpg"] },
    { date: "2023-04-01", recipient: "Tunde", proofs: ["proof4.jpg"] },
  ];

  return (
    <div className="container">
      <h1>Group History</h1>

      <div className="card">
        <table className="table history-table">
          <thead>
            <tr>
              <th>Date</th>
              <th>Payout Recipient</th>
              <th>Payment Proofs</th>
            </tr>
          </thead>
          <tbody>
            {history.map((item, index) => (
              <tr key={index}>
                <td>{item.date}</td>
                <td>{item.recipient}</td>
                <td>
                  {item.proofs.map((proof, i) => (
                    <span key={i}>
                      <a href={`/proofs/${proof}`} target="_blank" rel="noopener noreferrer">
                        [Proof {i+1}]
                      </a>{' '}
                    </span>
                  ))}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default HistoryPage;
