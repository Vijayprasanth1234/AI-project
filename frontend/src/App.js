import React, { useState } from "react";
import axios from "axios";

const API_BASE = process.env.REACT_APP_API_BASE || "http://44.221.124.81:5000";

function ChatMessage({ m }) {
  return (
    <div style={{ display: "flex", marginBottom: 8, justifyContent: m.role === "user" ? "flex-end" : "flex-start" }}>
      <div style={{ maxWidth: "75%", padding: 12, borderRadius: 8, background: m.role === "user" ? "#DCF8C6" : "#fff", boxShadow: "0 1px 3px rgba(0,0,0,0.06)" }}>
        {m.type === "recommendations" ? (
          m.payload.map((r, i) => (
            <div key={i} style={{ marginBottom: 8 }}>
              <div style={{ fontWeight: 600 }}>Instance: {r.inst}</div>
              <pre style={{ whiteSpace: "pre-wrap" }}>{r.llm && r.llm.text}</pre>
            </div>
          ))
        ) : (
          <div>{m.content || JSON.stringify(m.payload)}</div>
        )}
      </div>
    </div>
  );
}

function App() {
  const [messages, setMessages] = useState([{ role: "assistant", content: "Hello — ask me about cost optimization (e.g., 'List idle EC2 instances').", type: "text" }]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const send = async () => {
    if (!input.trim()) return;
    const userMsg = { role: "user", content: input, type: "text" };
    setMessages([...messages, userMsg]);
    setInput("");
    setLoading(true);
    try {
      const res = await axios.post(`${API_BASE}/chat`, { message: input });
      const botMsg = { role: "assistant", ...res.data };
      setMessages([...messages, userMsg, botMsg]);
    } catch (err) {
      const botMsg = { role: "assistant", content: "Error: " + err.message, type: "text" };
      setMessages([...messages, userMsg, botMsg]);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: 20, maxWidth: 800, margin: "auto" }}>
      <h2>AWS Cost Optimization Chatbot</h2>
      <div style={{ border: "1px solid #ddd", padding: 10, minHeight: 400, marginBottom: 10, overflowY: "auto" }}>
        {messages.map((m, i) => <ChatMessage key={i} m={m} />)}
      </div>
      <div style={{ display: "flex" }}>
        <input style={{ flex: 1, padding: 8 }} value={input} onChange={(e) => setInput(e.target.value)} placeholder="Type your question..." />
        <button onClick={send} disabled={loading} style={{ marginLeft: 8 }}>Send</button>
      </div>
    </div>
  );
}

export default App;
// Before

// After
const BACKEND_URL = "http://44.221.124.81:5000/api/cost";
