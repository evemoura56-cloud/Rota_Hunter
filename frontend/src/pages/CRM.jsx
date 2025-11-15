import { useState } from "react";
import styles from "./CRM.module.css";
import { KanbanBoard } from "../components/KanbanBoard";

export const CRM = ({ colunas, onMove, onCreate }) => {
  const [form, setForm] = useState({ nome: "", setor: "", status: "PROSPECTADO" });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onCreate(form);
    setForm({ nome: "", setor: "", status: "PROSPECTADO" });
  };

  return (
    <div className={styles.wrapper}>
      <form className={styles.formQuick} onSubmit={handleSubmit}>
        <input placeholder="Empresa" name="nome" value={form.nome} onChange={handleChange} required />
        <input placeholder="Setor" name="setor" value={form.setor} onChange={handleChange} />
        <select name="status" value={form.status} onChange={handleChange} style={{ padding: 12, borderRadius: 12, background: "#111", color: "#fff" }}>
          {Object.keys(colunas).map((status) => (
            <option key={status}>{status}</option>
          ))}
        </select>
        <button type="submit">Adicionar ao funil</button>
      </form>
      <KanbanBoard colunas={colunas} onMove={onMove} />
    </div>
  );
};
