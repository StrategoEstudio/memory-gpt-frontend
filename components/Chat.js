"use client";

import { useState } from "react";

const Chat = () => {
  const [userId] = useState("test_user");
  const [message, setMessage] = useState("");
  const [conversation, setConversation] = useState([]);

  const sendMessage = async (e) => {
    e.preventDefault();

    const newMessage = { user: "Tú", text: message };
    setConversation([...conversation, newMessage]);

    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/chat/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ user_id: userId, message })
      });

      if (response.ok) {
        const data = await response.json();
        const botMessage = { user: "Chatbot", text: data.response };
        setConversation((prev) => [...prev, botMessage]);
      } else {
        throw new Error("Error en la API");
      }
    } catch (error) {
      console.error("Error:", error);
      const errorMessage = { user: "Chatbot", text: "Error de conexión con el servidor" };
      setConversation((prev) => [...prev, errorMessage]);
    } finally {
      setMessage("");
    }
  };

  return (
    <div>
      <h2>Chatbot con Memoria</h2>
      <div style={{ border: "1px solid #ccc", padding: "10px", maxHeight: "300px", overflowY: "auto" }}>
        {conversation.map((msg, index) => (
          <div key={index} style={{ marginBottom: "10px" }}>
            <strong>{msg.user}:</strong> {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={sendMessage} style={{ marginTop: "10px" }}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Escribe un mensaje..."
          style={{ width: "80%", marginRight: "10px" }}
        />
        <button type="submit">Enviar</button>
      </form>
    </div>
  );
};

export default Chat;
