import { useState } from "react";
import styles from "./WhatsApp.module.css";
import { WhatsList } from "../components/WhatsList";

export const WhatsApp = ({ contatos }) => {
  const [mensagem, setMensagem] = useState("Olá {{nome}}, podemos falar sobre homologação?");

  const contatosFormatados = contatos.map((contato) => ({ ...contato, mensagem }));

  return (
    <div className={styles.section}>
      <div className={styles.card}>
        <h3>Mensagem padrão</h3>
        <textarea value={mensagem} onChange={(e) => setMensagem(e.target.value)} />
      </div>
      <WhatsList contatos={contatosFormatados} />
    </div>
  );
};
