// Minimal ZIM article extractor using libzim (Homebrew)
// Compile: clang++ -std=c++17 -o zim_extract zim_extract.cpp -lzim -L/opt/homebrew/lib
// Run: ./zim_extract <zim_file> <output_dir>

#include <zim/archive.h>
#include <zim/item.h>
#include <zim/blob.h>
#include <zim/entry.h>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>

namespace fs = std::filesystem;

std::string cleanFilename(const std::string& url) {
    std::string out;
    for (char c : url) {
        if (c == '/' || c == '\\' || c == ':' || c == '*' || c == '?' || c == '"' || c == '<' || c == '>') {
            out += '_';
        } else {
            out += c;
        }
    }
    return out;
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <zim_file> <output_dir>" << std::endl;
        return 1;
    }
    
    std::string zimPath = argv[1];
    std::string outDir = argv[2];
    fs::create_directories(outDir);
    
    try {
        std::cout << "Opening: " << zimPath << std::endl;
        zim::Archive archive(zimPath);
        
        auto articleCount = archive.getArticleCount();
        auto entryCount = archive.getEntryCount();
        std::cout << "Entries: " << entryCount << ", Articles: " << articleCount << std::endl;
        
        int extracted = 0;
        int skipped_redirects = 0;
        int skipped_images = 0;
        
        for (size_t i = 0; i < entryCount; ++i) {
            try {
                auto entry = archive.getEntryByPath(i);
                
                if (entry.isRedirect()) {
                    skipped_redirects++;
                    continue;
                }
                
                zim::Item item = entry.getItem();
                std::string mime = item.getMimetype();
                
                // Skip non-text content
                if (mime.find("text/") != 0) {
                    skipped_images++;
                    continue;
                }
                
                zim::Blob blob = item.getData();
                std::string url = entry.getPath();
                size_t dataSize = blob.size();
                
                // Determine extension
                std::string ext = ".txt";
                if (mime == "text/html") ext = ".html";
                
                std::string filename = cleanFilename(url);
                if (filename.empty()) filename = "entry_" + std::to_string(i);
                
                std::string outPath = (fs::path(outDir) / (filename + ext)).string();
                
                std::ofstream out(outPath, std::ios::binary);
                if (out) {
                    out.write(static_cast<const char*>(blob.data()), dataSize);
                    out.close();
                    
                    if (ext == ".html" || (ext == ".txt" && dataSize > 500)) {
                        std::cout << "[OK] " << filename << ext 
                                  << " (" << mime << ", " << dataSize << " bytes)" << std::endl;
                    }
                    extracted++;
                }
                
            } catch (const std::exception& e) {
                // Skip problematic entries silently
            }
            
            if ((i + 1) % 1000 == 0) {
                std::cout << "Progress: " << (i+1) << "/" << entryCount 
                          << " | extracted: " << extracted << std::endl;
            }
        }
        
        std::cout << "\nDone. Extracted " << extracted << " text articles." << std::endl;
        std::cout << "Skipped: " << skipped_redirects << " redirects, " 
                  << skipped_images << " non-text" << std::endl;
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
