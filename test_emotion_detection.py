from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test_str1 = "I am glad this happened"
        result1 = emotion_detector(test_str1)
        self.assertEqual(result1["dominant_emotion"], "joy")
        
        test_str2 = "I am really mad about this	"
        result2 = emotion_detector(test_str2)
        self.assertEqual(result2["dominant_emotion"], "anger")

        test_str3 = "I feel disgusted just hearing about this"
        result3 = emotion_detector(test_str3)
        self.assertEqual(result3["dominant_emotion"], "disgust")

        test_str4 = "I am so sad about this"
        result4 = emotion_detector(test_str4)
        self.assertEqual(result4["dominant_emotion"], "sadness")

        test_str5 = "I am really afraid that this will happen"
        result5 = emotion_detector(test_str5)
        self.assertEqual(result5["dominant_emotion"], "fear")

unittest.main()