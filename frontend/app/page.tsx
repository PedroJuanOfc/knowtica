import ArticleCard from "./components/ArticleCard";

interface Article {
  id: number;
  title: string;
  source: string;
  url: string;
  published_at: string;
  summary_short: string | null;
  summary_medium: string | null;
  summary_long: string | null;
}

export default async function Home({
  searchParams,
}: {
  searchParams: Promise<{ page?: string }>;
}) {
  const { page: pageParam } = await searchParams;
  const page = Number(pageParam) || 1;
  const limit = 5;
  const skip = (page - 1) * limit;
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/articles?skip=${skip}&limit=${limit}`,
    { cache: "no-store" },
  );
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
        <div className="flex justify-between mt-6">
          {page > 1 && (
            <a
              href={`/?page=${page - 1}`}
              className="px-4 py-2 text-sm border border-gray-300 rounded-full text-gray-600 hover:border-gray-500"
            >
              ← Previous
            </a>
          )}
          {articles.length === limit && (
            <a
              href={`/?page=${page + 1}`}
              className="px-4 py-2 text-sm border border-gray-300 rounded-full text-gray-600 hover:border-gray-500 ml-auto"
            >
              Next →
            </a>
          )}
        </div>
      </div>
    </main>
  );
}
