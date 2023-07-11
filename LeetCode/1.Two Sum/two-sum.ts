function twoSum(nums: number[], target: number): number[] {
    let hashmap = new Map();
    for (let i = 0; i < nums.length; i++) {
        const difference = target - nums[i];
        if (Array.from(hashmap.keys()).includes(difference)) {
            return [hashmap.get(difference), i];
        }
        hashmap.set(nums[i], i);
    }
    return [];
};
