import { useState } from "react";
import styles from "./HunterForm.module.css";

export const HunterForm = ({ onDiscover }) => {
  const [setor, setSetor] = useState("Tecnologia");
  const [regiao, setRegiao] = useState("Sudeste");
  const [keywords, setKeywords] = useState("dados, supply chain");
  const [observacoes, setObservacoes] = useState("Priorizar empresas com base instalada SAP");

  const handleSubmit = (event) => {
    event.preventDefault();
    onDiscover({ setor, regiao, keywords, observacoes });
  };

  return (
    <form className={styles.formCard} onSubmit={handleSubmit}>
      <div className={styles.row}>
        <label className={styles.field}>
          Setor alvo
          <input value={setor} onChange={(e) => setSetor(e.target.value)} />
        </label>
        <label className={styles.field}>
          Região preferencial
          <input value={regiao} onChange={(e) => setRegiao(e.target.value)} />
        </label>
      </div>
      <div className={styles.row}>
        <label className={styles.field}>
          Palavras chave
          <input value={keywords} onChange={(e) => setKeywords(e.target.value)} />
        </label>
      </div>
      <label className={styles.field}>
        Observações
        <textarea value={observacoes} onChange={(e) => setObservacoes(e.target.value)} />
      </label>
      <button className={styles.button} type="submit">
        Acionar Motor Hunter
      </button>
    </form>
  );
};
