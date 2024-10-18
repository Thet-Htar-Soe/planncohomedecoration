import { useState } from "react";
import axios from "axios";

function App() {
  const [input, setInput] = useState("");
  const [chatLog, setChatLog] = useState([]);

  const handleSend = async () => {
    if (!input) return;
    setChatLog([...chatLog, { sender: "user", message: input }]);

    try {
      const response = await axios.post("http://127.0.0.1:5000/api/chat", { prompt: input });
      setChatLog([...chatLog, { sender: "user", message: input }, { sender: "bot", message: response.data.response }]);
    } catch (error) {
      setChatLog([...chatLog, { sender: "bot", message: "Error: Could not get response." }]);
      console.log("this is error", error);
    }

    setInput("");
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Chatbot With OpenAI</h1>
      <div style={{ border: "1px solid #ccc", padding: "10px", height: "300px", overflowY: "scroll" }}>
        {chatLog.map((chat, idx) => (
          <div key={idx} style={{ textAlign: chat.sender === "user" ? "right" : "left" }}>
            <p>
              <strong>{chat.sender}:</strong> {chat.message}
            </p>
          </div>
        ))}
      </div>

      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type a message..."
        style={{ width: "80%", padding: "10px", marginTop: "10px" }}
      />
      <button onClick={handleSend} style={{ padding: "10px" }}>
        Send
      </button>
    </div>
  );
}

export default App;
