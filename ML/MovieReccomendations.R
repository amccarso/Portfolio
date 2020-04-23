#matrix factorization for Movie Recommendation System
#By Austin McCarson
#for Harvard edx Intro to Data Science: Machine Learning 
#lazy use of libraries
library(dslabs)
data("movielens")
head(movielens)
library(caret)
set.seed(755)

#split data into train and test set
test_index <- createDataPartition(y = movielens$rating, times = 1, p = 0.2, list = FALSE)
#set training set as second set of data in test_index
train_set <- movielens[-test_index,]
library(magrittr)
library(dplyr)

#join movieId and userId data set
test_set <- train_set %>%
  semi_join(train_set, by = "movieId") %>%
  semi_join(train_set, by = "userId")

#create RMSE function
RMSE <- function(true_ratings, predicted_ratings) {
  sqrt(mean((true_ratings - predicted_ratings)^2))
}
  
#find average rating in training set
mu_hat <- mean(train_set$rating)
#calculate RMSE for rating in training set
naive_rmse <- RMSE(test_set$rating, mu_hat)

#create predictions set
predictions <- rep(2.5, nrow(test_set))

#store results as dataframe
rmse_results <- data_frame(method = "Just the average", RMSE = naive_rmse)
#fit the model using lm
fit <- lm(rating ~ as.factor(userId), data = movielens)
#find the average of the rating in the training set
mu <- mean(train_set$rating)
#calculate and store average movie ratings
movie_avgs <- train_set %>%
  group_by(movieId) %>%
  summarize(b_i = mean(rating - mu))
#calculate predicted movie ratings
predicted_ratings <- mu + test_set %>%
  left_join(movie_avgs, by = 'movieId') %>%
  .$b_i

#calculate rmse for model
model_1_rmse <- RMSE(predicted_ratings, test_set$rating)
#store results for rmse
rmse_results <- bind_rows(rmse_results, 
                          data_frame(method = "Movie Effect Model",
                                     RMSE = model_1_rmse ))
#display as table
rmse_results %>% knitr::kable()

#calculate average ratings from users
user_avgs <- test_set %>%
  left_join(movie_avgs, by = 'movieId') %>%
  group_by(userId) %>%
  summarize(b_u = mean(rating - mu - b_i))
#calculate what we expect each user to rate
predicted_ratings <- test_set %>%
  left_join(movie_avgs, by = 'movieId') %>%
  left_join(user_avgs, by = 'userId') %>%
  mutate(pred = mu + b_i + b_u) %>%
  .$pred

#calculate rmse
model_2_rmse <- RMSE(predicted_ratings, test_set$rating)
#store results for rmse
rmse_results <- bind_rows(rmse_results, 
                          data_frame(method = "Movie + User Effects Model",
                                     RMSE = model_2_rmse ))

rmse_results %>% knitr::kable()