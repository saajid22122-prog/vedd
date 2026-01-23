"""
Test script for grammar analysis to verify word-level parsing
"""
import sys
import os
sys.path.append(os.path.dirname(__file__))

from groq_client import GroqClient
import json

def test_grammar_analysis():
    """Test different sentence scenarios"""
    client = GroqClient()
    
    test_cases = [
        {
            "sentence": "நான் school போனேன்",
            "description": "Mixed language (English word in Tamil)"
        },
        {
            "sentence": "நான் பள்ளி போனேன்",
            "description": "Missing location particle (க்கு)"
        },
        {
            "sentence": "நான் பள்ளிக்கு போனேன்",
            "description": "Correct sentence"
        },
        {
            "sentence": "நான் book படிக்கிறேன்",
            "description": "Mixed language with reading"
        },
    ]
    
    print("=" * 80)
    print("GRAMMAR ANALYSIS TEST RESULTS")
    print("=" * 80)
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test {i}: {test['description']}")
        print(f"Input: {test['sentence']}")
        print("-" * 80)
        
        result = client.analyze_grammar(test['sentence'], "Tamil")
        
        print(f"Is Correct: {result.get('is_correct')}")
        print(f"Corrected: {result.get('corrected_sentence')}")
        print(f"Mistake Type: {result.get('mistake_type')}")
        print(f"Explanation: {result.get('explanation')}")
        
        word_corrections = result.get('word_corrections', [])
        if word_corrections:
            print(f"\nWord-Level Corrections ({len(word_corrections)}):")
            for j, correction in enumerate(word_corrections, 1):
                print(f"  {j}. '{correction.get('original')}' → '{correction.get('corrected')}'")
                print(f"     Reason: {correction.get('reason')}")
        else:
            print("\nNo word-level corrections")
        
        print(f"\n{'='*80}")
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    test_grammar_analysis()
