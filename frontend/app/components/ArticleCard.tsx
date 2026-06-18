"use client";
import { useState } from "react";

interface Article {
  id: number;
  title: string;
  source: string;
  url: string;
  summary_short: string | null;
  summary_medium: string | null;
  summary_long: string | null;
}

export default function ArticleCard({ article }: { article: Article }) {
  const [activeFormat, setActiveFormat] = useState<
    "short" | "medium" | "long" | null
  >(null);

  const summaries = {
    short: article.summary_short,
    medium: article.summary_medium,
    long: article.summary_long,
  };

  return (
    <div className="bg-white border border-gray-200 rounded-xl p-6">
      <div className="flex justify-between items-start gap-4 mb-1">
        <a
          href={article.url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-lg font-bold text-gray-900 hover:underline"
        >
          {article.title}
        </a>
      </div>
      <p className="text-sm text-gray-400 mb-4">{article.source}</p>

      {activeFormat && (
        <div className="text-gray-700 text-sm leading-relaxed mb-4 border-l-2 border-gray-200 pl-4 flex flex-col gap-6">
          {summaries[activeFormat]?.split("\n\n").map((paragraph, index) => (
            <p key={index}>{paragraph}</p>
          ))}
        </div>
      )}

      <div className="flex gap-2">
        {(["short", "medium", "long"] as const).map((format) => (
          <button
            key={format}
            onClick={() =>
              setActiveFormat(activeFormat === format ? null : format)
            }
            className={`px-4 py-1.5 text-sm rounded-full border transition-colors ${
              activeFormat === format
                ? "bg-gray-900 text-white border-gray-900"
                : "text-gray-600 border-gray-300 hover:border-gray-500"
            }`}
          >
            {format.charAt(0).toUpperCase() + format.slice(1)}
          </button>
        ))}
      </div>
    </div>
  );
}
