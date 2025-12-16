import React, { useState } from 'react';
import { uploadJson, generateImage, generateVideo } from './services/api';
import type { ProjectData } from './types';
import FileUploader from './components/FileUploader';
import SceneList from './components/SceneList';
import { LayoutDashboard, Settings, History } from 'lucide-react';

function App() {
  const [projectData, setProjectData] = useState<ProjectData | null>(null);
  const [loading, setLoading] = useState(false);
  const [generatingTasks, setGeneratingTasks] = useState<Record<string, string>>({}); // taskId -> status
  const [generatedFiles, setGeneratedFiles] = useState<Record<string, string>>({}); // taskId -> fileUrl

  const handleUpload = async (file: File) => {
    setLoading(true);
    try {
      const data = await uploadJson(file);
      setProjectData(data);
    } catch (error) {
      console.error('Upload failed:', error);
      alert('Failed to upload JSON file');
    } finally {
      setLoading(false);
    }
  };

  const handleGenerateImage = async (sceneId: string, shotId: string, type: string, prompt: string) => {
    if (!projectData) return;
    
    const taskId = `${sceneId}-${shotId}-${type}`;
    setGeneratingTasks(prev => ({ ...prev, [taskId]: 'generating' }));

    try {
      const result = await generateImage({
        project_name: projectData.project,
        scene_id: sceneId,
        shot_id: shotId,
        prompt: prompt,
        frame_type: type
      });
      setGeneratingTasks(prev => ({ ...prev, [taskId]: 'completed' }));
      if (result.file_url) {
        setGeneratedFiles(prev => ({ ...prev, [taskId]: result.file_url }));
      }
    } catch (error) {
      console.error('Generation failed:', error);
      setGeneratingTasks(prev => ({ ...prev, [taskId]: 'failed' }));
    }
  };

  const handleGenerateVideo = async (sceneId: string, shotId: string, prompt: string) => {
    if (!projectData) return;
    
    const taskId = `${sceneId}-${shotId}-video`;
    setGeneratingTasks(prev => ({ ...prev, [taskId]: 'generating' }));

    try {
      const result = await generateVideo({
        project_name: projectData.project,
        scene_id: sceneId,
        shot_id: shotId,
        prompt: prompt,
      });
      setGeneratingTasks(prev => ({ ...prev, [taskId]: 'completed' }));
      if (result.file_url) {
        setGeneratedFiles(prev => ({ ...prev, [taskId]: result.file_url }));
      }
    } catch (error) {
      console.error('Video Generation failed:', error);
      setGeneratingTasks(prev => ({ ...prev, [taskId]: 'failed' }));
    }
  };

  return (
    <div className="min-h-screen bg-[#0f1115] text-gray-200 font-sans">
      {/* Sidebar (Simplified) */}
      <aside className="fixed left-0 top-0 h-full w-16 bg-[#161b22] border-r border-gray-800 flex flex-col items-center py-6 gap-6 z-10">
        <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center font-bold text-white mb-4">
          AI
        </div>
        <nav className="flex flex-col gap-4">
          <button className="p-2 text-blue-400 bg-blue-400/10 rounded-lg"><LayoutDashboard size={20} /></button>
          <button className="p-2 text-gray-500 hover:text-gray-300"><History size={20} /></button>
          <button className="p-2 text-gray-500 hover:text-gray-300"><Settings size={20} /></button>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="ml-16 p-8 max-w-7xl mx-auto">
        <header className="mb-10 flex justify-between items-end">
          <div>
            <h1 className="text-3xl font-bold text-white mb-2">Project Workspace</h1>
            <p className="text-gray-400">Manage and generate content for your AI video project</p>
          </div>
          {projectData && (
             <div className="text-right">
                <h2 className="text-xl font-semibold text-blue-400">{projectData.project}</h2>
                <span className="text-sm text-gray-500">{projectData.scenes.length} Scenes Loaded</span>
             </div>
          )}
        </header>

        {!projectData ? (
          <div className="max-w-2xl mx-auto mt-20">
             <FileUploader onUpload={handleUpload} isLoading={loading} />
          </div>
        ) : (
          <div className="space-y-6">
             {/* Project Info / Stats could go here */}
             
             {/* Scene List */}
             <SceneList 
                scenes={projectData.scenes}
                onGenerateImage={handleGenerateImage}
                onGenerateVideo={handleGenerateVideo}
                generatingTasks={generatingTasks}
                generatedFiles={generatedFiles}
             />
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
