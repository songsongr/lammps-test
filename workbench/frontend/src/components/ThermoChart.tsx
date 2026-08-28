/** 热力学曲线: LAMMPS thermo 样本折线图 (recharts), 序列可勾选 */
import { useMemo, useState } from "react";
import {
  CartesianGrid,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import type { ThermoData } from "../api/client";

const PALETTE = ["#3547e8", "#12994e", "#e5484d", "#0e9384", "#d97706", "#7c5cfc", "#64748b"];
const CANDIDATE_SERIES = ["Temp", "PotEng", "E_pair", "TotEng", "KinEng", "Press", "Volume"];
const MAX_POINTS = 1000; // 渲染上限, 超出取最近

export default function ThermoChart({ data }: { data: ThermoData }) {
  const available = useMemo(
    () => CANDIDATE_SERIES.filter((c) => data.columns.includes(c)),
    [data.columns],
  );
  const [visible, setVisible] = useState<Set<string>>(
    () => new Set(available.slice(0, 3)),
  );

  const chartData = useMemo(
    () =>
      data.rows.slice(-MAX_POINTS).map((row) => {
        const point: Record<string, number> = {};
        data.columns.forEach((c, i) => {
          point[c] = row[i];
        });
        return point;
      }),
    [data],
  );

  if (!data.columns.length || !data.rows.length) return null;
  const stepKey = data.columns[0]; // 恒为 "Step"

  const toggle = (c: string) => {
    setVisible((prev) => {
      const next = new Set(prev);
      if (next.has(c)) next.delete(c);
      else next.add(c);
      return next;
    });
  };

  return (
    <div>
      <div style={{ display: "flex", flexWrap: "wrap", gap: 14, marginBottom: 8 }}>
        {available.map((c, i) => (
          <label
            key={c}
            style={{
              display: "inline-flex",
              alignItems: "center",
              gap: 6,
              fontSize: 12.5,
              fontWeight: 550,
              color: visible.has(c) ? PALETTE[i % PALETTE.length] : "var(--text-3)",
              cursor: "pointer",
              userSelect: "none",
            }}
          >
            <input
              type="checkbox"
              checked={visible.has(c)}
              onChange={() => toggle(c)}
              style={{ accentColor: PALETTE[i % PALETTE.length] }}
            />
            {c}
          </label>
        ))}
      </div>
      <ResponsiveContainer width="100%" height={240}>
        <LineChart data={chartData} margin={{ top: 6, right: 12, bottom: 0, left: 0 }}>
          <CartesianGrid stroke="rgba(29,29,26,0.07)" vertical={false} />
          <XAxis
            dataKey={stepKey}
            tick={{ fontSize: 11, fill: "#a3a39a" }}
            tickLine={false}
            axisLine={{ stroke: "rgba(29,29,26,0.12)" }}
            domain={["dataMin", "dataMax"]}
          />
          <YAxis
            width={62}
            tick={{ fontSize: 11, fill: "#a3a39a" }}
            tickLine={false}
            axisLine={false}
            domain={["auto", "auto"]}
          />
          <Tooltip
            contentStyle={{
              borderRadius: 10,
              border: "1px solid rgba(29,29,26,0.1)",
              boxShadow: "0 4px 16px rgba(25,25,20,0.08)",
              fontSize: 12,
            }}
          />
          {available.map(
            (c, i) =>
              visible.has(c) && (
                <Line
                  key={c}
                  type="monotone"
                  dataKey={c}
                  stroke={PALETTE[i % PALETTE.length]}
                  strokeWidth={1.6}
                  dot={false}
                  isAnimationActive={false}
                />
              ),
          )}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
