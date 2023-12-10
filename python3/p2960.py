class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:

        tested_devices = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                tested_devices += 1
                for j in range(i + 1, len(batteryPercentages)):
                    # not sure why it says min must not go below zero; doesn't seem to matter for end result
                    batteryPercentages[j] -= 1

        return tested_devices