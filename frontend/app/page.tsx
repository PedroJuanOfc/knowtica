import ArticleCard from "./components/ArticleCard";

interface Article {
  id: number;
  title: string;
  source: string;
  url: string;
  summary_short: string | null;
  summary_medium: string | null;
  summary_long: string | null;
}

export default async function Home() {
  const response = await fetch("http://127.0.0.1:8000/articles");
  const articles = await response.json();
  return (
    <main className="max-w-2xl mx-auto px-4 py-12">
      <div className="mb-10">
        <p className="text-xs font-semibold uppercase tracking-widest text-blue-600 mb-2">
          Knowtica
        </p>
        <h1 className="text-4xl font-bold text-gray-900 mb-2">
          News at your pace.
        </h1>
        <p className="text-gray-500">
          Skim the headlines. Expand any story into a short, medium or long
          summary — without leaving the page.
        </p>
      </div>
      <div className="flex flex-col gap-4">
        {articles.map((article: Article) => (
          <ArticleCard key={article.id} article={article} />
        ))}
      </div>
    </main>
  );
}
