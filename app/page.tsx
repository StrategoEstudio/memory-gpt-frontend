// Importa el componente Chat desde la carpeta components
import Chat from "../components/Chat"; // Asegúrate de que esta ruta es correcta

// Componente principal de la página
export default function Home() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Memory GPT Chat</h1>
      {/* Renderiza el componente Chat */}
      <Chat />
    </div>
  );
}
