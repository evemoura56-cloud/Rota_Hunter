import { useState } from "react";
import styles from "./TemplateManager.module.css";

export const TemplateManager = ({ templates, onSave }) => {
  const [selecionado, setSelecionado] = useState(templates[0]);
  const [conteudo, setConteudo] = useState(templates[0].corpo);

  const trocar = (template) => {
    setSelecionado(template);
    setConteudo(template.corpo);
  };

  const salvar = () => onSave({ ...selecionado, corpo: conteudo });

  return (
    <div className={styles.manager}>
      <div className={styles.list}>
        {templates.map((template) => (
          <div key={template.id} onClick={() => trocar(template)} className={styles.template} style={{ borderColor: template.id === selecionado.id ? "var(--verm-neon)" : "rgba(255, 46, 76, 0.25)" }}>
            <strong>{template.nome}</strong>
            <p style={{ margin: 0, color: "var(--cinza-claro)" }}>{template.assunto}</p>
          </div>
        ))}
      </div>
      <div className={styles.editor}>
        <h4>{selecionado.nome}</h4>
        <textarea value={conteudo} onChange={(e) => setConteudo(e.target.value)} />
        <div className={styles.actions}>
          <button className={styles.secondary} type="button" onClick={() => navigator.clipboard.writeText(conteudo)}>
            Copiar
          </button>
          <button className={styles.primary} type="button" onClick={salvar}>
            Salvar
          </button>
        </div>
      </div>
    </div>
  );
};
