import styles from "./CompanyList.module.css";

export const CompanyList = ({ empresas }) => (
  <div className={styles.list}>
    {empresas.map((empresa) => (
      <div key={empresa.id} className={styles.card}>
        <div>
          <div className={styles.company}>{empresa.nome}</div>
          <div className={styles.details}>
            {empresa.setor} · {empresa.regiao} · {empresa.site}
          </div>
        </div>
        <span className={styles.tag}>{empresa.prioridade}</span>
      </div>
    ))}
  </div>
);
