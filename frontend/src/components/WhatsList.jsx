import styles from "./WhatsList.module.css";

export const WhatsList = ({ contatos }) => {
  const gerarLink = (numero, mensagem) => `https://wa.me/${numero}?text=${encodeURIComponent(mensagem)}`;

  return (
    <div className={styles.list}>
      {contatos.map((contato) => (
        <div key={contato.id} className={styles.card}>
          <div>
            <h4>{contato.nome}</h4>
            <small>{contato.cargo} · {contato.empresa}</small>
          </div>
          <button className={styles.button} onClick={() => window.open(gerarLink(contato.whatsapp, contato.mensagem), "_blank")}>Enviar</button>
        </div>
      ))}
    </div>
  );
};
