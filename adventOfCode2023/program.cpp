#include <iostream>
#include <fstream>
#include <vector>
#include <thread>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <map>
#include <set>
#include <mutex>

std::mutex mtx;

void transformValues(std::vector<int>& lookingFor, const std::vector<std::vector<int>>& df, const std::vector<int>& nxt, int start, int end) {
    for (int i = start; i < end; ++i) {
        std::set<int> visited;
        std::map<int, int> transform;

        for (const auto& elem : df[i]) {
            for (int j = 0; j < lookingFor.size(); ++j) {
                int l = lookingFor[j];
                int diff = l - elem[1];
                if (l >= elem[1] && diff < elem[2]) {
                    transform[j] = elem[0] + diff;
                    visited.insert(j);
                }
            }
        }

        std::vector<int> nxtLocal;
        for (int j = 0; j < lookingFor.size(); ++j) {
            if (visited.count(j) > 0) {
                nxtLocal.push_back(transform[j]);
            } else {
                nxtLocal.push_back(lookingFor[j]);
            }
        }

        std::lock_guard<std::mutex> lock(mtx);
        lookingFor = nxtLocal;
    }
}

int main() {
    std::ifstream file("day05.txt");

    if (!file.is_open()) {
        std::cerr << "Error opening file." << std::endl;
        return 1;
    }

    int count = 0;
    std::vector<int> lookingFor, nxt;
    std::string inputString;
    std::string last = "seed";
    std::map<std::string, std::vector<std::vector<int>>> df;
    std::vector<std::string> index;

    for (std::string line; std::getline(file, line); ) {
        if (line.empty()) {
            continue;
        } else if (line.compare(0, 5, "seeds") == 0) {
            nxt = {std::istream_iterator<int>(std::istringstream(line.substr(6))), std::istream_iterator<int>()};
        } else if (isdigit(line[0])) {
            df[last].push_back({std::istream_iterator<int>(std::istringstream(line)), std::istream_iterator<int>()});
        } else if (!isdigit(line[0])) {
            last = line.substr(0, line.find(' '));
            df[last] = {};
            index.push_back(last);
        }
    }

    for (int i = 0; i < nxt.size(); i += 2) {
        for (int j = nxt[i]; j < nxt[i] + nxt[i + 1]; ++j) {
            lookingFor.push_back(j);
        }
    }

    std::vector<std::thread> threads;
    const int numThreads = std::thread::hardware_concurrency();
    const int batchSize = index.size() / numThreads;

    for (int i = 0; i < numThreads; ++i) {
        int start = i * batchSize;
        int end = (i == numThreads - 1) ? index.size() : (i + 1) * batchSize;
        threads.emplace_back(transformValues, std::ref(lookingFor), std::ref(df[index]), std::ref(nxt), start, end);
    }

    for (auto& thread : threads) {
        thread.join();
    }

    std::cout << "Result: " << *std::min_element(lookingFor.begin(), lookingFor.end()) << std::endl;

    return 0;
}
