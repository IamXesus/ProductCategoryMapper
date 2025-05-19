from pyspark.sql.functions import col

def get_product_category_pairs(spark, products_df, categories_df, product_categories_df):
    products = products_df.alias('p')
    product_categories = product_categories_df.alias('pc')
    categories = categories_df.alias('c')

    product_category_join = products.join(
        product_categories,
        col('p.id') == col('pc.product_id'),
        how='left'
    )

    result_df = product_category_join.join(
        categories,
        col('pc.category_id') == col('c.id'),
        how='left'
    )

    result_df = result_df.select(
        col('p.name').alias('product_name'),
        col('c.name').alias('category_name')
    )

    return result_df