from pyspark.sql import SparkSession
from src.utils import get_product_category_pairs

if __name__ == "__main__":
    spark = SparkSession.builder.appName("ProductCategoryTest").getOrCreate()


    products_data = [(1, "ProductA"), (2, "ProductB"), (3, "ProductC")]
    products_df = spark.createDataFrame(products_data, ["id", "name"])

    categories_data = [(10, "CategoryX"), (20, "CategoryY")]
    categories_df = spark.createDataFrame(categories_data, ["id", "name"])

    product_categories_data = [(1, 10), (1, 20), (2, 10)]
    product_categories_df = spark.createDataFrame(product_categories_data, ["product_id", "category_id"])


    result = get_product_category_pairs(spark, products_df, categories_df, product_categories_df)
    result.show()

    spark.stop()