import React from 'react';
import { Scene, Shot } from '../types';
import { Film, Image as ImageIcon, Video, Play, CheckCircle2, AlertCircle, Loader2 } from 'lucide-react';

interface SceneListProps {
    scenes: Scene[];
    onGenerateImage: (sceneId: string, shotId: string, type: string, prompt: string) => void;
    onGenerateVideo: (sceneId: string, shotId: string, prompt: string) => void;
    generatingTasks: Record<string, string>; // key: taskId (e.g. "sceneId-shotId-type"), value: status
    generatedFiles: Record<string, string>; // key: taskId, value: fileUrl
}

const SceneList: React.FC<SceneListProps> = ({ scenes, onGenerateImage, onGenerateVideo, generatingTasks, generatedFiles }) => {
    
    const getTaskStatus = (id: string) => generatingTasks[id];
    const getFileUrl = (id: string) => generatedFiles[id];

    return (
        <div className="space-y-8">
            {scenes.map((scene) => (
                <div key={scene.scene_id} className="bg-gray-900 rounded-xl overflow-hidden border border-gray-800">
                    <div className="p-4 border-b border-gray-800 bg-gray-800/50 flex items-center justify-between">
                        <div className="flex items-center gap-3">
                            <Film className="text-blue-400 w-5 h-5" />
                            <h3 className="font-semibold text-lg text-white">
                                {scene.scene_id}: {scene.scene_title || 'Untitled Scene'}
                            </h3>
                        </div>
                        <span className="text-sm text-gray-400 bg-gray-800 px-2 py-1 rounded">
                            {scene.timestamp || 'No Timestamp'}
                        </span>
                    </div>
                    
                    <div className="divide-y divide-gray-800">
                        {scene.shots.map((shot) => (
                            <ShotItem 
                                key={shot.shot_id} 
                                shot={shot} 
                                sceneId={scene.scene_id}
                                onGenerateImage={onGenerateImage}
                                onGenerateVideo={onGenerateVideo}
                                getStatus={getTaskStatus}
                                getFileUrl={getFileUrl}
                            />
                        ))}
                    </div>
                </div>
            ))}
        </div>
    );
};

interface ShotItemProps {
    shot: Shot;
    sceneId: string;
    onGenerateImage: (sceneId: string, shotId: string, type: string, prompt: string) => void;
    onGenerateVideo: (sceneId: string, shotId: string, prompt: string) => void;
    getStatus: (id: string) => string | undefined;
    getFileUrl: (id: string) => string | undefined;
}

const ShotItem: React.FC<ShotItemProps> = ({ shot, sceneId, onGenerateImage, onGenerateVideo, getStatus, getFileUrl }) => {
    return (
        <div className="p-4 hover:bg-gray-800/30 transition-colors">
            <div className="flex items-start justify-between mb-3">
                <div>
                    <div className="flex items-center gap-2 mb-1">
                        <span className="text-xs font-mono text-blue-300 bg-blue-900/30 px-1.5 py-0.5 rounded">
                            {shot.shot_id}
                        </span>
                        <h4 className="font-medium text-gray-200">{shot.name || shot.description || 'Shot'}</h4>
                    </div>
                    {shot.description && (
                        <p className="text-sm text-gray-500 line-clamp-2">{shot.description}</p>
                    )}
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
                {/* Image Generation Section */}
                {shot.nano_banana_pro_prompts && (
                    <div className="bg-gray-950/50 rounded-lg p-3 border border-gray-800">
                        <div className="flex items-center gap-2 mb-3 text-sm text-gray-400">
                            <ImageIcon className="w-4 h-4" />
                            <span>Keyframes</span>
                        </div>
                        <div className="space-y-2">
                            {['start', 'middle', 'end'].map((frame) => {
                                const prompt = (shot.nano_banana_pro_prompts as any)[frame];
                                if (!prompt) return null;
                                const taskId = `${sceneId}-${shot.shot_id}-${frame}`;
                                const status = getStatus(taskId);
                                const fileUrl = getFileUrl(taskId);

                                return (
                                    <div key={frame} className="space-y-2 bg-gray-900 p-2 rounded border border-gray-800/50">
                                        <div className="flex items-center justify-between gap-3">
                                            <div className="flex flex-col min-w-0 flex-1">
                                                <span className="text-xs font-bold text-gray-500 uppercase">{frame}</span>
                                                <p className="text-xs text-gray-400 truncate" title={prompt}>{prompt}</p>
                                            </div>
                                            <ActionButton 
                                                status={status} 
                                                onClick={() => onGenerateImage(sceneId, shot.shot_id, frame, prompt)}
                                                label="Gen"
                                            />
                                        </div>
                                        {fileUrl && (
                                            <div className="relative aspect-video rounded overflow-hidden bg-black/50 border border-gray-800">
                                                <img 
                                                    src={`http://localhost:8000${fileUrl}`} 
                                                    alt={`${frame} frame`}
                                                    className="w-full h-full object-contain"
                                                />
                                            </div>
                                        )}
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                )}

                {/* Video Generation Section */}
                {shot.veo_3_1_prompt && (
                    <div className="bg-gray-950/50 rounded-lg p-3 border border-gray-800">
                        <div className="flex items-center gap-2 mb-3 text-sm text-gray-400">
                            <Video className="w-4 h-4" />
                            <span>Video Generation</span>
                        </div>
                        <div className="bg-gray-900 p-3 rounded border border-gray-800/50 mb-3">
                            <p className="text-xs text-gray-400 line-clamp-3" title={shot.veo_3_1_prompt}>
                                {shot.veo_3_1_prompt}
                            </p>
                        </div>
                        {getFileUrl(`${sceneId}-${shot.shot_id}-video`) && (
                             <div className="mb-3 relative aspect-video rounded overflow-hidden bg-black/50 border border-gray-800">
                                <video 
                                    src={`http://localhost:8000${getFileUrl(`${sceneId}-${shot.shot_id}-video`)}`} 
                                    controls
                                    className="w-full h-full object-contain"
                                />
                            </div>
                        )}
                        <div className="flex justify-end">
                            <ActionButton 
                                status={getStatus(`${sceneId}-${shot.shot_id}-video`)} 
                                onClick={() => onGenerateVideo(sceneId, shot.shot_id, shot.veo_3_1_prompt!)}
                                label="Generate Video"
                                icon={<Play className="w-3 h-3 mr-1.5" />}
                                className="w-full justify-center"
                            />
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

interface ActionButtonProps {
    status?: string;
    onClick: () => void;
    label: string;
    icon?: React.ReactNode;
    className?: string;
}

const ActionButton: React.FC<ActionButtonProps> = ({ status, onClick, label, icon, className = "" }) => {
    if (status === 'completed') {
        return (
            <button className={`flex items-center text-xs text-green-400 bg-green-900/20 px-3 py-1.5 rounded border border-green-900/50 cursor-default ${className}`}>
                <CheckCircle2 className="w-3 h-3 mr-1" />
                Done
            </button>
        );
    }
    
    if (status === 'generating') {
        return (
            <button className={`flex items-center text-xs text-blue-400 bg-blue-900/20 px-3 py-1.5 rounded border border-blue-900/50 cursor-wait ${className}`} disabled>
                <Loader2 className="w-3 h-3 mr-1 animate-spin" />
                Wait
            </button>
        );
    }

    if (status === 'failed') {
         return (
            <button onClick={onClick} className={`flex items-center text-xs text-red-400 bg-red-900/20 px-3 py-1.5 rounded border border-red-900/50 hover:bg-red-900/30 ${className}`}>
                <AlertCircle className="w-3 h-3 mr-1" />
                Retry
            </button>
        );
    }

    return (
        <button 
            onClick={onClick}
            className={`flex items-center text-xs text-gray-300 bg-gray-800 hover:bg-blue-600 hover:text-white px-3 py-1.5 rounded border border-gray-700 transition-colors ${className}`}
        >
            {icon}
            {label}
        </button>
    );
};

export default SceneList;
