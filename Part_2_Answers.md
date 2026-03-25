# Q1 Choosing the Right Approach 

## You are tasked with identifying whether a product is missing its label on an assembly line. The products are visually similar except for the label.

## Q: Would you use classification, detection, or segmentation? Why? What would be your fallback if the first approach doesn’t work?


I would use object detection for this task because the goal is to identify whether a label is present on the product, and the label occupies only a small region of the image. 

Classification may fail because the overall appearance of the product is similar with or without the label, so the model may not focus on the correct region. 

Detection allows the model to explicitly localize the label and determine whether it exists. 

If detection does not work well, my fallback would be segmentation to precisely identify the label region. Segmentation could help when labels are small, partially visible, or have irregular shapes. 

However, I would start with detection because it is simpler and faster to train.



# Q2 — Debugging a Poorly Performing Model

## You trained a model on 1000 images, but it performs poorly on new images from the factory.

## Q: Design a small experiment or checklist to debug the issue. What would you test or visualize?


If the model performs poorly on new factory images, I would first check whether the training data distribution matches the new data. I would visualize predictions on both training and new images to see where the model fails. 

Next, I would check for overfitting by comparing training and validation metrics. I would also inspect annotations to ensure labels are correct and consistent. 

Another step would be to test the model on different lighting conditions, angles, and backgrounds to see if domain shift is the issue. 

If needed, I would collect more data from the factory environment and retrain the model.



# Q3 — Accuracy vs Real Risk

## Your model has 98% accuracy but still misses 1 out of 10 defective products.

## Q: Is accuracy the right metric in this case? What would you look at instead and why?


Accuracy is not the best metric in this case because missing defective products is more costly than incorrectly flagging good ones. A model with high accuracy can still fail if the dataset is imbalanced. 

I would instead look at recall for the defective class, because we want to detect as many defects as possible. Precision is also important, but recall is critical for safety or quality control systems. 

I would also analyze the confusion matrix to understand the types of errors the model makes. In real-world systems, the cost of false negatives must be considered more than overall accuracy.



# Q4 — Annotation Edge Cases

## You’re labeling data, but many images contain blurry or partially visible objects.

## Q: Should these be kept in the dataset? Why or why not? What trade-offs are you considering?


Blurry or partially visible objects should usually be kept in the dataset because real-world data often contains such cases. Removing them can make the model perform well on clean data but fail in production. However, these cases should be labeled carefully to avoid confusing the model. 

The trade-off is between dataset quality and realism. Too many noisy labels can reduce performance, but too much filtering can reduce generalization. I would keep these images but ensure consistent annotation rules. This helps the model become more robust to real-world conditions.