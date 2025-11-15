import { useEffect, useRef } from "react";
import { createChart } from "lightweight-charts";
import styles from "./ChartSection.module.css";

const chartOptions = {
  layout: {
    background: { color: "transparent" },
    textColor: "#fff",
  },
  grid: {
    vertLines: { color: "rgba(255, 255, 255, 0.1)" },
    horzLines: { color: "rgba(255, 255, 255, 0.1)" },
  },
  timeScale: {
    visible: false,
  },
};

const barChartOptions = {
  ...chartOptions,
  rightPriceScale: {
    borderVisible: false,
  },
  timeScale: {
    borderVisible: false,
  },
};

const lineChartOptions = {
  ...chartOptions,
  rightPriceScale: {
    borderVisible: false,
  },
  timeScale: {
    borderVisible: false,
  },
};

export const ChartSection = ({ pizza, barras, linha }) => {
  const barChartRef = useRef(null);
  const lineChartRef = useRef(null);

  useEffect(() => {
    const barChart = createChart(barChartRef.current, barChartOptions);
    const barSeries = barChart.addHistogramSeries({
      color: "#ff2e4c",
      priceFormat: {
        type: "volume",
      },
    });
    barSeries.setData(barras.map((item) => ({ time: item.nome, value: item.valor })));
    barChart.timeScale().fitContent();

    const lineChart = createChart(lineChartRef.current, lineChartOptions);
    const lineSeries = lineChart.addLineSeries({ color: "#ff2e4c", lineWidth: 2 });
    lineSeries.setData(linha.map((item) => ({ time: item.dia, value: item.valor })));
    lineChart.timeScale().fitContent();

    return () => {
      barChart.remove();
      lineChart.remove();
    };
  }, [barras, linha]);

  return (
    <div className={styles.section}>
      <div className={styles.panel}>
        <h4>Distribuição por Setor</h4>
        <div className={styles.pieAlternative}>
          {pizza.map((item, index) => (
            <div key={index} className={styles.pieItem}>
              <span className={styles.pieColor} style={{ backgroundColor: ["#ff2e4c", "#b3122c", "#e6e6e6", "#ff6273", "#ff94a3"][index % 5] }}></span>
              <span>{item.nome}</span>
              <span>{item.valor}</span>
            </div>
          ))}
        </div>
      </div>
      <div className={styles.panel} ref={barChartRef} />
      <div className={styles.panel} ref={lineChartRef} />
    </div>
  );
};
