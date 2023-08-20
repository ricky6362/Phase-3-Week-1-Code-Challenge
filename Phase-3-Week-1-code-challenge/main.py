from Author import Author
from Magazine import Magazine
from Article import Article

# Create instances for testing
author1 = Author("Michael Johnson")
author2 = Author("Emily White")
magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Fashion Weekly", "Fashion")

article1 = Article(author1, magazine1, "The Future of AI")
article2 = Article(author1, magazine2, "Summer Fashion Trends")
article3 = Article(author2, magazine1, "Ethical Considerations in AI")
article4 = Article(author2, magazine2, "Sustainable Fashion Choices")

# Example: Print the names of all authors
print("Authors:")
for author in Author.all():
    print(author.name())

# Example: Print the names of all magazines
print("\nMagazines:")
for magazine in Magazine.all():
    print(magazine.name())

# Example: Print the titles of all articles
print("\nArticle Titles:")
for article in Article.all():
    print(article.title())

# Example: Test article author() and magazine() methods
print("\nArticle Author and Magazine:")
print(article1)
print(article2)

# Example: Test author articles() and magazines() methods
print("\nAuthor's Articles and Magazines:")
for author in Author.all():
    print(f"{author.name()}:")
    for article in author.articles():
        print(f"  {article.title()} in {article.magazine().name()}")

# Example: Test magazine contributors() method
print("\nMagazine Contributors:")
for magazine in Magazine.all():
    print(f"{magazine.name()}:")
    for contributor in magazine.contributors():
        print(f"  {contributor.name()}")

# Example: Test author add_article() and topic_areas() methods
new_article = author1.add_article(magazine1, "AI Ethics in Healthcare")
print("\nNew Article:")
print(new_article)
print(f"{author1.name()}'s Articles:")
for article in author1.articles():
    print(f"  {article.title()} in {article.magazine().name()}")
print(f"{author1.name()}'s Topic Areas: {', '.join(author1.topic_areas())}")

# Example: Test magazine find_by_name() and article_titles() methods
found_magazine = Magazine.find_by_name("Fashion Weekly")
print("\nFound Magazine:")
print(found_magazine)
print("Article Titles:")
for title in found_magazine.article_titles():
    print(f"  {title}")

# Example: Test magazine contributing_authors() method
print("\nContributing Authors:")
for magazine in Magazine.all():
    print(f"{magazine.name()}")
    for contributor in magazine.contributing_authors():
        print(f"  {contributor.name()}")
