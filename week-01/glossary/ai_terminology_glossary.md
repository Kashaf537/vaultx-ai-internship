# **AI Terminology Glossary**

## **1. Token**

LLMs can't read text directly. Instead, they convert words into small pieces known as tokens to better process the text.
For example :
"I love Python!" (Simple sentence)
"I" "love" "Python" "!" (Tokenize form)

## **2. Context Window**

A context window is basically the amount of information or text a model can consider at a time.

## **3. Temperature**

Temperature controls how creative and random a model's output can be. At a low temperature, the variation in output is usually low, and the responses tend to be more predictable. At a high temperature, the model can produce more varied and creative responses.

## **4. Top-p**

Top-p determines how large a group of likely options the model considers when choosing the next tokens.

## **5. System Prompt**

A system prompt is a set of instructions given to the model that defines its role, goals, and constraints.

## **6. Embedding**

An embedding is a numerical representation of text that captures its semantic meaning and helps compare the relationships between different pieces of text.

## **7. Hallucination**

A hallucination occurs when a model confidently generates information that is incorrect or unsupported. Instead of admitting that it doesn't know a fact, the model may produce a fabricated answer.

## **8. Fine-tuning**

Fine-tuning is the process of training a pretrained model on specialized or domain-specific data so that it performs better for a particular task or domain.

## **9. Inference**

Inference is the process of using a trained model to produce an output from new input.

## **Base Model vs Instruction-Tuned Model**

### **Base Model**

A base model is a model that has gone through its main pretraining process and learned patterns from large amounts of data.

### **Instruction-Tuned Model**

An instruction-tuned model is a pretrained model that undergoes additional training to become better at following human instructions.

## **Why LLMs Predict Text Instead of "Knowing" Facts**

LLMs are trained to predict the next token based on patterns they learned from large amounts of training data. They use these learned patterns to generate responses that may appear knowledgeable, but they do not actually store and understand facts like humans do. Because they generate text based on learned patterns, they can sometimes produce information that is incorrect or fabricated.