# Lab 4 - Problem 1: Customer Email Classification

def generate_email_prompts():
    print("--- PROBLEM 1: EMAIL CLASSIFICATION ---")
    
    # Test Email
    test_email = "I have been charged twice for my subscription this month. Please refund the extra amount."
    
    # Zero-Shot
    print("\n[ZERO-SHOT PROMPT]")
    print(f"Classify the following email into one of these categories: Billing, Technical Support, Feedback, Others.")
    print(f"Email: \"{test_email}\"")
    
    # One-Shot (With 1 Example)
    print("\n[ONE-SHOT PROMPT]")
    print("Example 1: \"My internet connection is very slow.\" -> Technical Support")
    print(f"Now classify this email: \"{test_email}\"")
    
    # Few-Shot (With 3 Examples)
    print("\n[FEW-SHOT PROMPT]")
    print("Example 1: \"The app crashes when I open settings.\" -> Technical Support")
    print("Example 2: \"I love the new dark mode feature!\" -> Feedback")
    print("Example 3: \"Where can I find my invoice?\" -> Billing")
    print(f"Now classify this email: \"{test_email}\"")
    print("-" * 30)

generate_email_prompts()




# Lab 4 - Problem 2: Chatbot Intent Classification

def generate_chatbot_prompts():
    print("--- PROBLEM 2: CHATBOT INTENTS ---")
    
    # Test Query
    test_query = "Where is my package? It was supposed to arrive today."
    
    # Zero-Shot
    print("\n[ZERO-SHOT PROMPT]")
    print(f"Classify this query into: Account Issue, Order Status, Product Inquiry, General Question.")
    print(f"Query: \"{test_query}\"")
    
    # One-Shot
    print("\n[ONE-SHOT PROMPT]")
    print("Example: \"How do I reset my password?\" -> Account Issue")
    print(f"Now classify: \"{test_query}\"")
    
    # Few-Shot
    print("\n[FEW-SHOT PROMPT]")
    print("Example 1: \"Does this laptop have 16GB RAM?\" -> Product Inquiry")
    print("Example 2: \"What are your opening hours?\" -> General Question")
    print("Example 3: \"I cannot login to my portal.\" -> Account Issue")
    print(f"Now classify: \"{test_query}\"")
    print("-" * 30)

generate_chatbot_prompts()




# Lab 4 - Problem 3: Student Feedback Analysis

def generate_feedback_prompts():
    print("--- PROBLEM 3: FEEDBACK ANALYSIS ---")
    
    test_feedback = "The course content is good, but the audio quality needs improvement."
    
    # Zero-Shot
    print("\n[ZERO-SHOT PROMPT]")
    print(f"Classify the sentiment of this feedback as Positive, Negative, or Neutral.")
    print(f"Feedback: \"{test_feedback}\"")
    
    # Few-Shot
    print("\n[FEW-SHOT PROMPT]")
    print("Example 1: \"This is the best course ever!\" -> Positive")
    print("Example 2: \"I wasted my money on this.\" -> Negative")
    print("Example 3: \"It was okay, nothing special.\" -> Neutral")
    print(f"Now classify: \"{test_feedback}\"")
    print("-" * 30)

generate_feedback_prompts()




# Lab 4 - Problem 4: Course Recommendation

def generate_course_prompts():
    print("--- PROBLEM 4: COURSE LEVEL ---")
    
    test_query = "I want to learn how to implement deep learning using PyTorch."
    
    # Zero-Shot
    print("\n[ZERO-SHOT PROMPT]")
    print(f"Classify this learner query as Beginner, Intermediate, or Advanced.")
    print(f"Query: \"{test_query}\"")
    
    # Few-Shot
    print("\n[FEW-SHOT PROMPT]")
    print("Example 1: \"What is a variable in Python?\" -> Beginner")
    print("Example 2: \"How do I use Lambda functions with lists?\" -> Intermediate")
    print("Example 3: \"Optimizing neural network weights.\" -> Advanced")
    print(f"Now classify: \"{test_query}\"")
    print("-" * 30)

generate_course_prompts()




# Lab 4 - Problem 5: Content Moderation

def generate_moderation_prompts():
    print("--- PROBLEM 5: SOCIAL MEDIA MODERATION ---")
    
    test_post = "Click this link to win a free iPhone instantly!!! limited time offer!"
    
    # Zero-Shot
    print("\n[ZERO-SHOT PROMPT]")
    print(f"Classify this post as Acceptable, Offensive, or Spam.")
    print(f"Post: \"{test_post}\"")
    
    # Few-Shot
    print("\n[FEW-SHOT PROMPT]")
    print("Example 1: \"Just had a great lunch with friends.\" -> Acceptable")
    print("Example 2: \"You are stupid and nobody likes you.\" -> Offensive")
    print("Example 3: \"Earn $5000 from home, ask me how!\" -> Spam")
    print(f"Now classify: \"{test_post}\"")
    print("-" * 30)

generate_moderation_prompts()