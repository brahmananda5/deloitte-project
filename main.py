import json, unittest, datetime

with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)

def convertFromFormat1 (jsonObject):

    result = {}

    # copy required fields (adjust keys if needed as per data-result.json)
    result["deviceId"] = jsonObject["id"]
    result["temperature"] = jsonObject["temperature"]

    # ISO timestamp → milliseconds
    iso_time = jsonObject["timestamp"]
    dt = datetime.datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    result["timestamp"] = int(dt.timestamp() * 1000)

    return result



def convertFromFormat2 (jsonObject):

    result = {}

    result["deviceId"] = jsonObject["device"]["id"]
    result["temperature"] = jsonObject["telemetry"]["temperature"]

    # already in milliseconds
    result["timestamp"] = jsonObject["telemetry"]["timestamp"]

    return result



class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    unittest.main()

  
