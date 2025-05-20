from pyspark.sql import SparkSession

from src.my_module import create_dataframes
from src.utils import get_product_category_pairs

if __name__ == "__main__":
    spark = SparkSession.builder.appName("ProductCategoryTest").getOrCreate()

    products_df, categories_df, product_categories_df = create_dataframes(spark)

    result = get_product_category_pairs(spark, products_df, categories_df, product_categories_df)
    result.show()

    spark.stop()