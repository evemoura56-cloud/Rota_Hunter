import styles from "./IATable.module.css";

export const IATable = ({ registros }) => (
  <table className={styles.table}>
    <thead>
      <tr>
        <th>#</th>
        <th>Empresa</th>
        <th>Setor</th>
        <th>p_win</th>
        <th>Motivo</th>
      </tr>
    </thead>
    <tbody>
      {registros.map((linha, index) => (
        <tr key={linha.id} style={{ background: index % 2 === 0 ? "rgba(255,255,255,0.02)" : "transparent" }}>
          <td className={styles.rank}>{index + 1}</td>
          <td>{linha.empresa}</td>
          <td>{linha.setor}</td>
          <td>
            <span className={styles.badge}>{linha.pwin}%</span>
          </td>
          <td>{linha.motivo}</td>
        </tr>
      ))}
    </tbody>
  </table>
);
